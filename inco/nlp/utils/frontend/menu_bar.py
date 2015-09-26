from Tkinter import Menu, Toplevel, StringVar
import codecs
import tkFileDialog
from ttk import *

from inco.nlp.utils.frontend.configuration_manager import ConfigurationManager


__author__ = 'Matias Laino'


class MenuBar:
    __settings_file_name = "config.txt"

    read_delegate = None

    def open_configuration(self):
        filewin = Toplevel(self.parent)
        filewin.wm_title('Configuration')
        filewin.wm_transient(self.parent)

        i = 0

        label = Label(filewin, text="Configure path to binaries")
        label.grid(row=i, column=0)
        i += 1

        label = Label(filewin, text="FreeLing")
        label.grid(row=i, column=0)
        entry_freeling = Entry(filewin, width=100, textvariable=self.var_freeling_path)
        entry_freeling.grid(row=i, column=1)
        control = Button(filewin, text="Browse...", command=self.browse_freeling)
        control.grid(row=1, column=2)
        i += 1

        label = Label(filewin, text="TreeTagger")
        label.grid(row=i, column=0)
        entry_treetagger = Entry(filewin, width=100, textvariable=self.var_treetagger_path)
        entry_treetagger.grid(row=i, column=1)
        control = Button(filewin, text="Browse...", command=self.browse_treetagger)
        control.grid(row=i, column=2)
        i += 1

        label = Label(filewin, text="MaltParser")
        label.grid(row=i, column=0)
        entry_maltparser = Entry(filewin, width=100, textvariable=self.var_maltparser_path)
        entry_maltparser.grid(row=i, column=1)
        control = Button(filewin, text="Browse...", command=self.browse_maltparser)
        control.grid(row=i, column=2)
        i += 1

        label = Label(filewin, text="MaltParser Spanish model")
        label.grid(row=i, column=0)
        entry = Entry(filewin, width=100, textvariable=self.var_maltparser_model_path)
        entry.grid(row=i, column=1)
        control = Button(filewin, text="Browse...", command=self.browse_maltparser_model)
        control.grid(row=i, column=2)
        i += 1

        label = Label(filewin, text="Stanford Shift-Reduce")
        label.grid(row=i, column=0)
        entry = Entry(filewin, width=100, textvariable=self.var_stanfordsr_path)
        entry.grid(row=i, column=1)
        control = Button(filewin, text="Browse...", command=self.browse_stanfordsr)
        control.grid(row=i, column=2)
        i += 1

        label = Label(filewin, text="Stanford SR Spanish model")
        label.grid(row=i, column=0)
        entry = Entry(filewin, width=100, textvariable=self.var_stanfordsr_model_path)
        entry.grid(row=i, column=1)
        control = Button(filewin, text="Browse...", command=self.browse_stanfordsr_model)
        control.grid(row=i, column=2)
        i += 1

        control = Button(filewin, text="Apply", command=self.__apply_configuration)
        control.grid(row=i, columnspan=2)

        # load saved settings
        settings = ConfigurationManager.load()
        if settings is not None:
            self.var_freeling_path.set(settings['freeling_path'])
            self.var_treetagger_path.set(settings['treetagger_path'])
            self.var_maltparser_path.set(settings['maltparser_path'])
            self.var_maltparser_model_path.set(settings['maltparser_model_path'])
            self.var_stanfordsr_path.set(settings['stanfordsr_path'])
            self.var_stanfordsr_model_path.set(settings['stanfordsr_model_path'])

        self.read_delegate = None

    def __apply_configuration(self):
        ConfigurationManager.save(self.var_freeling_path.get(),
                                  self.var_treetagger_path.get(),
                                  self.var_maltparser_path.get(),
                                  self.var_maltparser_model_path.get(),
                                  self.var_stanfordsr_path.get(),
                                  self.var_stanfordsr_model_path.get(),
        )

    def browse_freeling(self):
        filename = tkFileDialog.askopenfilename(filetypes=(("Windows executable files", "*.exe"),
                                                           ("All files", "*.*")))
        self.var_freeling_path.set(filename)


    def browse_maltparser(self):
        filename = tkFileDialog.askopenfilename(filetypes=(("JAR files", "*.jar"),
                                                           ("All files", "*.*")))
        self.var_maltparser_path.set(filename)


    def browse_maltparser_model(self):
        filename = tkFileDialog.askopenfilename(filetypes=(("MaltParser model files", "*.mco"),
                                                           ("All files", "*.*")))
        self.var_maltparser_model_path.set(filename)

    def browse_treetagger(self):
        filename = tkFileDialog.askopenfilename(filetypes=(("Batch files", "*.bat"),
                                                           ("All files", "*.*")))
        self.var_treetagger_path.set(filename)

    def browse_stanfordsr(self):
        filename = tkFileDialog.askopenfilename(filetypes=(("JAR files", "*.jar"),
                                                           ("All files", "*.*")))
        self.var_stanfordsr_path.set(filename)

    def browse_stanfordsr_model(self):
        filename = tkFileDialog.askopenfilename()
        self.var_stanfordsr_model_path.set(filename)

    def __init__(self, parent):
        self.parent = parent

        menubar = Menu(self.parent)
        menubar.add_command(label="Configuration", command=self.open_configuration)

        self.var_freeling_path = StringVar()
        self.var_maltparser_path = StringVar()
        self.var_maltparser_model_path = StringVar()
        self.var_treetagger_path = StringVar()
        self.var_stanfordsr_model_path = StringVar()
        self.var_stanfordsr_path = StringVar()

        parent.config(menu=menubar)
