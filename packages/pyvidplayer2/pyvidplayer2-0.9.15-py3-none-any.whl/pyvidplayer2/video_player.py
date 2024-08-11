import pygame
import cv2 
import math
from . import Video


class VideoPlayer:
    def __init__(self, video, rect, interactable=False, loop=False, preview_thumbnails=0):

        self.video = video
        self.frame_rect = pygame.Rect(rect)
        self.interactable = interactable
        self.loop = loop
        self.preview_thumbnails = min(max(preview_thumbnails, 0), self.video.frame_count)
        self._show_intervals = self.preview_thumbnails != 0

        self.vid_rect = pygame.Rect(0, 0, 0, 0)
        self._progress_back = pygame.Rect(0, 0, 0, 0)
        self._progress_bar = pygame.Rect(0, 0, 0, 0)
        self._smooth_bar = 0 # used for making the progress bar look smooth when seeking
        self._font = pygame.font.SysFont("arial", 0)

        self._buffer_rect = pygame.Rect(0, 0, 0, 0)
        self._buffer_angle = 0

        self._zoomed = False

        self._buffer_frame = None # updated with new video frames

        self._transform(self.frame_rect)

        self._show_ui = False
        self.queue_ = []

        self._clock = pygame.time.Clock()
        
        self._seek_pos = 0 
        self._seek_time = 0
        self._show_seek = False

        self._fade_timer = 0
        
        if self._show_intervals:
            self._interval = self.video.duration / self.preview_thumbnails
            self._interval_frames = []
            self._get_interval_frames()

    def __str__(self):
        return f"<VideoPlayer(path={self.path})>"

    def _close_queue(self):
        for video in self.queue_:
            try:
                video.close()
            except AttributeError:
                pass
    
    def _get_interval_frames(self):
        size = (int(70 * self.video.aspect_ratio), 70)
        for i in range(self.preview_thumbnails):
            self.video._vid.set(cv2.CAP_PROP_POS_FRAMES, int(i * self.video.frame_rate * self._interval))
            
            self._interval_frames.append(pygame.image.frombuffer(cv2.resize(self.video._vid.read()[1], dsize=size, interpolation=cv2.INTER_AREA).tobytes(), size, "BGR"))

        # add last readable frame

        i = 1
        while True:
            self.video._vid.set(cv2.CAP_PROP_POS_FRAMES, self.video.frame_count - i)
            try:
                self._interval_frames.append(pygame.image.frombuffer(cv2.resize(self.video._vid.read()[1], dsize=size, interpolation=cv2.INTER_AREA).tobytes(), size, "BGR"))
            except:
                i += 1
            else:
                break 

        self.video._vid.set(cv2.CAP_PROP_POS_FRAMES, 0)
    
    def _get_closest_frame(self, time):
        i = math.floor(time // self._interval)
        if (i + 1) * self._interval - time >= self._interval // 2:
            return self._interval_frames[i]
        else:
            return self._interval_frames[i + 1]
        
    def _transform(self, rect):
        self.frame_rect = rect
        self.zoom_out()

        self._progress_back = pygame.Rect(self.frame_rect.x + 10, self.frame_rect.bottom - 25, self.frame_rect.w - 20, 15)
        self._progress_bar = self._progress_back.copy()

        self._font = pygame.font.SysFont("arial", 10)

        if self._buffer_frame is not None:
            self._buffer_frame = pygame.transform.smoothscale(self._buffer_frame, self.vid_rect.size)

        self._buffer_rect = pygame.Rect(0, 0, 200, 200)
        self._buffer_rect.center = self.frame_rect.center

    def _move_angle(self, pos, angle, distance):
        return pos[0] + math.cos(angle) * distance, pos[1] + math.sin(angle) * distance
    
    def _convert_seconds(self, time):
        return self.video._convert_seconds(time).split(".")[0]
    
    def zoom_to_fill(self):
        s = max(abs(self.frame_rect.w - self.vid_rect.w), abs(self.frame_rect.h - self.vid_rect.h))
        self.vid_rect.inflate_ip(s, s)
        self.video.resize(self.vid_rect.size)
        self._zoomed = True

    # takes a rect and an aspect ratio, returns the largest rect of the aspect ratio that can be fit inside
    
    def _best_fit(self, rect, r):
        s = rect.size
        r = self.video.aspect_ratio
        
        w = s[0]
        h = int(w / r)
        y = int(s[1] /2 - h / 2)
        x = 0
        if h > s[1]:
            h = s[1]
            w = int(h * r)
            x = int(s[0] / 2 - w / 2)
            y = 0
            
        return pygame.Rect(rect.x + x, rect.y + y, w, h)

    def zoom_out(self):
        self.vid_rect = self._best_fit(self.frame_rect, self.video.aspect_ratio)
        self.video.resize(self.vid_rect.size)
        self._zoomed = False

    def toggle_zoom(self):
        if self._zoomed:
            self.zoom_out()
        else:
            self.zoom_to_fill()

    def queue(self, input_):
        self.queue_.append(input_)

        # update once to trigger audio loading
        try:
            input_.stop()
            input_._update()
        except AttributeError:
            pass
        
    def resize(self, size):
        self.frame_rect.size = size
        self._transform(self.frame_rect)

    def move(self, pos, relative=False):
        if relative:
            self.frame_rect.move_ip(*pos)
        else:
            self.frame_rect.topleft = pos
        self._transform(self.frame_rect)

    def update(self, events=None, show_ui=None):
        dt = self._clock.tick()

        if not self.video.active:
            if self.queue_:
                if self.loop:
                    self.queue(self.video)
                input_ = self.queue_.pop(0)
                try:
                    self.video = Video(input_)
                except TypeError:
                    self.video = input_
                    self.video.play()
                self._transform(self.frame_rect)
            elif self.loop:
                self.video.restart()

        if self.video._update():
            self._buffer_frame = self.video.frame_surf   

        if self.interactable:

            mouse = pygame.mouse.get_pos()
            click = False 
            for event in events:
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    click = True

            self._show_ui = self.frame_rect.collidepoint(mouse) if show_ui is None else show_ui

            if self._show_ui:
                self._progress_bar.w = self._progress_back.w * (self.video.get_pos() / self.video.duration)
                self._smooth_bar += (self._progress_bar.w - self._smooth_bar) / (dt * 0.25)
                self._show_seek = self._progress_back.collidepoint(mouse)

                if self._show_seek:
                    t = (self._progress_back.w - (self._progress_back.right - mouse[0])) * (self.video.duration / self._progress_back.w)

                    self._seek_pos = self._progress_back.w * (round(t, 1) / self.video.duration) + self._progress_back.x
                    self._seek_time = t

                    if click:
                        self.video.seek(t, relative=False)
                        self.video.play()
                
                elif click:
                    self.video.toggle_pause()

        self._buffer_angle += dt / 10

        return self._show_ui

    def draw(self, win):
        pygame.draw.rect(win, "black", self.frame_rect)
        if self._buffer_frame is not None:
            win.blit(self._buffer_frame, self.vid_rect.topleft)

        if self._show_ui:
            pygame.draw.line(win, (50, 50, 50), (self._progress_back.x, self._progress_back.centery), (self._progress_back.right, self._progress_back.centery), 5)
            if self._smooth_bar > 1:
                pygame.draw.line(win, "white", (self._progress_bar.x, self._progress_bar.centery), (self._progress_bar.x + self._smooth_bar, self._progress_bar.centery), 5)

            f = self._font.render(self.video.name, True, "white")
            win.blit(f, (self.frame_rect.x + 10, self.frame_rect.y + 10))

            f = self._font.render(self._convert_seconds(self.video.get_pos()), True, "white")
            win.blit(f, (self.frame_rect.x + 10, self._progress_bar.top - f.get_height() - 10))

            if self._show_seek:
                pygame.draw.line(win, "white", (self._seek_pos, self._progress_back.top), (self._seek_pos, self._progress_back.bottom), 2)

                f = self._font.render(self._convert_seconds(self._seek_time), True, "white")
                win.blit(f, (self._seek_pos - f.get_width() // 2, self._progress_back.y - 10 - f.get_height()))

                if self._show_intervals:
                    surf = self._get_closest_frame(self._seek_time)
                    x = self._seek_pos - surf.get_width() // 2
                    x = min(max(x, self.frame_rect.x), self.frame_rect.right - surf.get_width())
                    pygame.draw.rect(win, (0, 0, 0), (x - 2, self._progress_back.y - 80 - f.get_height() - 2, surf.get_width() + 4, surf.get_height() + 4), 2)
                    win.blit(surf, (x, self._progress_back.y - 80 - f.get_height()))

        if self.interactable:
            if self.video.buffering:
                for i in range(6):
                    a = math.radians(self._buffer_angle + i * 60)
                    pygame.draw.line(win, "white", self._move_angle(self.frame_rect.center, a, 10), self._move_angle(self.frame_rect.center, a, 30))
            elif self.video.paused:
                pygame.draw.rect(win, "white", (self.frame_rect.centerx - 15, self.frame_rect.centery - 20, 10, 40))
                pygame.draw.rect(win, "white", (self.frame_rect.centerx + 5, self.frame_rect.centery - 20, 10, 40))

    def close(self):
        self.video.close()
        self._close_queue()
        
    def skip(self):
        self.video.stop() if self.loop else self.video.close()

    def get_next(self):
        return self.queue_[0] if self.queue_ else None
    
    def clear_queue(self):
        self._close_queue()
        self.queue_ = []

    def get_video(self):
        return self.video
    
    def get_queue(self):
        return self.queue_
