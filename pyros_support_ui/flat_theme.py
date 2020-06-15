################################################################################
# Copyright (C) 2020 Abstract Horizon
# All rights reserved. This program and the accompanying materials
# are made available under the terms of the Apache License v2.0
# which accompanies this distribution, and is available at
# https://www.apache.org/licenses/LICENSE-2.0
#
#  Contributors:
#    Daniel Sendula - initial API and implementation
#
#################################################################################

from pyros_support_ui.components import *


class ButtonDecoration(Component):
    def __init__(self, colour):
        super(ButtonDecoration, self).__init__(None)  # Call super constructor to store rectable
        self.colour = colour

    def draw(self, surface):
        pygame.draw.rect(surface, self.colour, self.rect)


class BorderDecoration(Component):
    def __init__(self, colour):
        super(BorderDecoration, self).__init__(None)  # Call super constructor to store rectable
        self.colour = colour

    def draw(self, surface):
        pygame.draw.rect(surface, self.colour, self.rect, 1)


class FlatThemeFactory(BaseUIFactory):
    def __init__(self, ui_adapter, font=None, small_font=None, colour=pygame.color.THECOLORS['cyan'], background_colour=pygame.color.THECOLORS['gray32'], mouse_over_colour=pygame.color.THECOLORS['lightgray']):
        super(FlatThemeFactory, self).__init__(ui_adapter,
                                               font=font,
                                               small_font=small_font,
                                               colour=colour,
                                               background_colour=background_colour,
                                               mouse_over_colour=mouse_over_colour)

    def setMouseOverColour(self, mouse_over_colour):
        self.mouse_over_colour = mouse_over_colour

    def setBackgroundColour(self, background_colour):
        self.background_colour = background_colour

    def label(self, rect, text, font=None, colour=None, h_alignment=ALIGNMENT.LEFT, v_alignment=ALIGNMENT.TOP, hint=UiHint.NORMAL):
        label = Label(rect, text, font=font if font is not None else self.font, colour=colour, h_alignment=h_alignment, v_alignment=v_alignment)
        return label

    def image(self, rect, image, h_alignment=ALIGNMENT.LEFT, v_alignment=ALIGNMENT.TOP, hint=UiHint.NORMAL):
        return Image(rect, image, h_alignment=h_alignment, v_alignment=v_alignment)

    def button(self, rect, on_click=None, on_hover=None, label=None, hint=UiHint.NORMAL):
        background_colour = self.background_colour
        mouse_over_colour = self.mouse_over_colour
        if hint == UiHint.WARNING:
            background_colour = pygame.color.THECOLORS['darkorange3']
            mouse_over_colour = pygame.color.THECOLORS['darkorange']
        elif hint == UiHint.ERROR:
            background_colour = pygame.color.THECOLORS['indianred4']
            mouse_over_colour = pygame.color.THECOLORS['indianred']

        return Button(rect, on_click, on_hover, label,
                      background_decoration=ButtonDecoration(background_colour),
                      mouse_over_decoration=ButtonDecoration(mouse_over_colour))

    def panel(self, rect, background_colour=None, hint=UiHint.NORMAL):
        if background_colour is None:
            if hint == UiHint.WARNING:
                background_colour = pygame.color.THECOLORS['orange']
            elif hint == UiHint.ERROR:
                background_colour = pygame.color.THECOLORS['red']
        return Panel(rect, background_colour, decoration=BorderDecoration(self.colour))

    def menu(self, rect, background_colour=None, hint=UiHint.NORMAL):
        if background_colour is None:
            if hint == UiHint.WARNING:
                background_colour = pygame.color.THECOLORS['orange']
            elif hint == UiHint.ERROR:
                background_colour = pygame.color.THECOLORS['red']
        return Menu(rect, self, background_colour, decoration=BorderDecoration(self.colour))