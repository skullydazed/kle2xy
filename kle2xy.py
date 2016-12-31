import hjson
from decimal import Decimal


class KLE2xy(list):
    """Abstract interface for interacting with a KLE layout.
    """
    def __init__(self, layout=None):
        super(KLE2xy, self).__init__()

        self.unit = 'mm'
        self.key_width = Decimal('19.05')
        self.key_skel = {
            'width': Decimal('1'), 'height': Decimal('1'),
            'x': Decimal('0'), 'y': Decimal('0')
        }

        if layout:
            self.parse_layout(layout)

    def parse_layout(self, layout):
        # Wrap this in a dictionary so hjson will parse KLE raw data
        layout = '{"layout": [' + layout + ']}'
        layout = hjson.loads(layout)['layout']

        # Initialize our state machine
        current_key = self.key_skel.copy()
        current_x = 0
        current_y = self.key_width / 2

        for row_num, row in enumerate(layout):
            self.append([])

            # Process the current row
            for key in row:
                if isinstance(key, dict):
                    if 'w' in key and key['w'] != Decimal(1):
                        current_key['width'] = Decimal(key['w'])
                    if 'h' in key and key['h'] != Decimal(1):
                        current_key['height'] = Decimal(key['h'])
                    continue

                else:
                    current_key['name'] = key

                    # Determine the X center
                    x_center = (current_key['width'] * self.key_width) / 2
                    current_x += x_center
                    current_key['x'] = current_x
                    current_x += x_center

                    # Determine the Y center
                    y_center = (current_key['height'] * self.key_width) / 2
                    y_offset = y_center - (self.key_width / 2)
                    current_key['y'] = -(current_y + y_offset)

                    # Store this key
                    self[-1].append(current_key)
                    current_key = self.key_skel.copy()

            # Move to the next row
            current_x = 0
            current_y += self.key_width
