import tkinter as tk

from ver.gui import mvc
from ver.gui.constants import Constants
from ver.gui.page1_frame import Page1Frame


# --------------------
## holds information for the "view" in MVC pattern
class View:
    # --------------------
    ## constructor
    def __init__(self):
        ## holds the parent window
        self._root = None
        ## holds the page1 frame
        self._page1_frame = None
        ## flags for menu item clicks
        self._nested1 = False
        self._nested2 = False
        self._hithere = False

    # --------------------
    ## initialize
    #
    # @return None
    def init(self):
        self._root = tk.Tk()
        mvc.guiapi.set_window(self._root)
        mvc.guiapi.set_name(self._root, 'window1')

        self._root.title(f'Ver Version: {Constants.version}')

        self._root.geometry('400x300')
        self._root.resizable(True, True)

        # Set exit cleanup function to be called on clicking 'x'
        self._root.protocol('WM_DELETE_WINDOW', self.abort)

        self._create_menu_bar()
        self._create_main_frame()

        mvc.logger.info('gui initialised')

    # --------------------
    ## start the main TKinter loop
    #
    # @return None
    def start_mainloop(self):
        self._root.mainloop()

    # --------------------
    ## gracefully shutdown the current session.
    #
    # @param signum  (not used) signal number
    # @param frame   (not used) the frame
    # @return None
    def abort(self, signum=None, frame=None):  # pylint: disable=unused-argument
        # at this point: ok to exit

        # Call the app which manages the other threads to trigger the exit.
        self._root.quit()

    # --------------------
    ## create the main page1 frame
    #
    # @return None
    def _create_main_frame(self):
        self._page1_frame = Page1Frame()
        frame = self._page1_frame.init(self._root)
        frame.grid(column=0, columnspan=1, row=1, rowspan=1, sticky=tk.NSEW)

        # TODO create page2 frame
        # TODO main window swaps between page1 and page2 frame
        # TODO center the frame; currently it goes to upper left

    # --------------------
    ## Creates and places the menu bar which is at the top of the application.
    #
    # @return None
    def _create_menu_bar(self) -> None:
        menu = tk.Menu(self._root)
        mvc.guiapi.set_menu(menu)
        self._root.config(menu=menu)

        file_menu = tk.Menu(menu, tearoff=False)
        menu.add_cascade(label='File', menu=file_menu)
        file_menu.add_command(label='later', command=self._on_hithere)

        menu2 = tk.Menu(file_menu)
        file_menu.add_cascade(label='Nested', menu=menu2)
        menu2.add_command(label='nested1', command=self._on_nested1)
        menu2.add_command(label='nested2', command=self._on_nested2)
        menu2.add_command(label='nested3', state=tk.DISABLED)

        file_menu.add_separator()
        file_menu.add_command(label='Exit', command=self.abort)

        menu.add_command(label="Clear", command=self._clear)

    # --------------------
    ## clear the page1 frame
    #
    # @return None
    def _clear(self):
        self._page1_frame.clear()

    # --------------------
    ## callback for menu item: File | Nested | nested1
    #
    # @return None
    def _on_nested1(self):
        mvc.logger.info('on_nested1: called')
        self._nested1 = True

    # --------------------
    ## callback for menu item: File | Nested | nested2
    #
    # @return None
    def _on_nested2(self):
        mvc.logger.info('on_nested2: called')
        self._nested2 = True

    # --------------------
    ## callback for menu item: File | later
    #
    # @return None
    def _on_hithere(self):
        mvc.logger.info('hi there')
        self._hithere = True

        # uncomment to debug
        # content = mvc.guiapi.get_screen()
        # import json
        # mvc.logger.info(f'DBG {json.dumps(content, indent=4)}')
        #
        # item = content['children'][1]['children'][2]['children'][10]  # combox1
        # mvc.logger.info(f'DBG {json.dumps(item, indent=4)}')
        # coord = item['coordinates']
        # x = int((coord['x1'] + coord['x2']) / 2)
        # y = int((coord['y1'] + coord['y2']) / 2)
        # mvc.logger.info(f'DBG x,y={x} {y}')
        # w = self._root.winfo_containing(x, y)
        # mvc.logger.info(f'DBG {w}')
        # mvc.logger.info(f'DBG {w.winfo_class()}')
        # n = getattr(w, 'guiapi_name', '<unknown>')
        # mvc.logger.info(f'DBG {n}')
        # mvc.logger.info(f'DBG num options: {w.index("end")}')
        # mvc.logger.info('DBG Combobox - use set')
        # val = 'combobox_opt1'
        # w.set(val)
        # w.event_generate('<<ComboboxSelected>>')
        #
        # content = mvc.guiapi.get_screen()
        # mvc.logger.info(f'DBG {json.dumps(content, indent=4)}')

        # TODO use tk.Dialog() to create a dlgbox
        # from tkinter import messagebox, simpledialog
        # messagebox.askokcancel('title', 'message')
        # content = mvc.guiapi.get_screen()
        # import json
        # mvc.logger.info(f'DBG {json.dumps(content, indent=4)}')

    # --------------------
    ## callback for handling additional GUI API commands
    # illustrates how to handle an incoming command
    #
    # @param   cmd the incoming command to handle
    # @return None
    def callback(self, cmd: dict) -> dict:
        rsp = {
            'rsp': cmd['cmd'],
        }
        if cmd['cmd'] == 'cmd01':
            self._handle_cmd01(cmd, rsp)
        elif cmd['cmd'] == 'getinfo':
            self._handle_getinfo(cmd, rsp)
        else:
            mvc.logger.info(f'view callback: unknown cmd={cmd["cmd"]}')
            rsp['value'] = 'nak'
            rsp['reason'] = 'cb: unknown command'

        return rsp

    # --------------------
    def _handle_cmd01(self, cmd: dict, rsp: dict):
        if 'param1' not in cmd:
            rsp['value'] = 'nak'
            rsp['reason'] = 'cb: missing param1'
            return

        if 'param2' not in cmd:
            rsp['value'] = 'nak'
            rsp['reason'] = 'cb: missing param2'
            return

        rsp['value'] = 'ack'
        mvc.logger.info(f'callback: cmd={cmd["cmd"]}')
        mvc.logger.info(f'   param1: {cmd["param1"]}')
        mvc.logger.info(f'   param2: {cmd["param2"]}')

    # --------------------
    def _handle_getinfo(self, cmd: dict, rsp: dict):
        rsp['nested1'] = self._nested1
        self._nested1 = False

        rsp['nested2'] = self._nested2
        self._nested2 = False

        rsp['hithere'] = self._hithere
        self._hithere = False

        rsp['value'] = 'ack'
