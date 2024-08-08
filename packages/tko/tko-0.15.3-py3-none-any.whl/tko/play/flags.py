from typing import List, Dict, Any
from ..util.ftext import Sentence

class Flag:
    def __init__(self):
        self._name: str = ""
        self._text: str = ""  # description
        self._char: str = ""
        self._values: List[str] = ["0", "1"]
        self._index: int = 0
        self._location: str = ""
        self._bool = True  # many options

    def name(self, _name):
        self._name = _name
        return self

    def text(self, _text):
        self._text = _text
        return self

    def char(self, _key):
        self._char = _key
        return self

    def values(self, _values: List[str]):
        self._values = _values
        return self

    def index(self, _index):
        self._index = _index
        return self

    def location(self, value: str):
        self._location = value
        return self

    def toggle(self):
        self._index = (self._index + 1) % len(self._values)
        return self

    def many(self):
        self._bool = False
        return self
    
    def bool(self):
        self._bool = True
        return self
    
    def is_bool(self):
        return self._bool

    def get_location(self) -> str:
        return self._location

    def get_value(self) -> str:
        return self._values[self._index % len(self._values)]

    def is_true(self):
        return self.get_value() == "1"

    def get_name(self) -> str:
        return self._name

    def get_description(self) -> str:
        return self._text

    def get_char(self) -> str:
        return self._char

    def get_index(self) -> int:
        return self._index

    def get_color(self) -> str:
        if self.get_value() == "1":
            return Flags.flag_on.get_value()
        return Flags.flag_off.get_value()

    def get_toggle_sentence(self, pad: int = 0) -> Sentence:
        if not self._bool:
            name = Sentence().addf(self.get_value(), f"{self._name}".ljust(pad))
            value = Sentence().add(f"[{self.get_char()}]").add(name).add(f"{self.get_value()}".rjust(2))
            return value
            
        char = self.get_char()
        text = self.get_name()
        color = self.get_color()
        extra = Sentence()
        if pad > 0:
            extra.addf(color, (pad - len(text)) * " ")
        value = Sentence().addf(color + "/", text).add(extra).addf("kW", f"[{char}]")
        return value
    

class Flags:
    minimum = Flag().name("Mínimo").char("m").values(["0", "1"]).text("Mostra os requisitos mínimos para completar a missão").location("left")
    reward = Flag().name("Recompensa").char("r").values(["0", "1"]).text("Mostra a experiência obtida na tarefa").location("left")
    percent = Flag().name("Percentual").char("p").values(["0", "1"]).text("Mostra valores em porcentagem").location("left")
    admin = Flag().name("Admin").char("A").text("Mostra todas as missões e grupos").location("left")
    fortune = Flag().name("Conselho").char("C").values(["1", "0"]).text("Mostra mensagem aleatórias na saída").location("left")
    success = Flag().name("Sucesso").char("S").values(["1", "0"]).text("Mostra os personagens no sucesso da execução").location("left")
    config = Flag().name("Config").char("c").values(["0", "1"]).text("Mostra a barra de flags").location("top")
    skills = Flag().name("Inventário").char("i").values(["0", "1"]).text("Mostra a barra de skills").location("top")

    focus     = Flag().name("Selected").values(["kB"]).text("Cor do item em foco").many()
    prog_done = Flag().name("ProgDone").values(["g"]).text("Progresso Done").many()
    prog_todo = Flag().name("ProgTodo").values(["y"]).text("Progresso Todo").many()
    flag_on   = Flag().name("Toggle_1").values(["G"]).text("Flag True").many()
    flag_off  = Flag().name("Toggle_0").values(["Y"]).text("Flag False").many()
    cmds      = Flag().name("Cmds").values(["B"]).text("CMDS").many()
    skill_done = Flag().name("ExpeDone").values(["G"]).text("Skill Done").many()
    skill_todo = Flag().name("ExpeTodo").values(["R"]).text("Skill Todo").many()
    main_done = Flag().name("MainDone").values(["B"]).text("Main Done").many()
    main_todo = Flag().name("MainTodo").values(["M"]).text("Main Todo").many()


class FlagsMan:
    def __init__(self, data: Dict[str, int]):
        self.flags: Dict[str, Flag] = {}
        self.left: List[Flag] = []
        self.top: List[Flag] = []

        for flag in Flags.__dict__.values():
            if isinstance(flag, Flag):
                self.flags[flag.get_name()] = flag
                if flag.get_location() == "left":
                    self.left.append(flag)
                elif flag.get_location() == "top":
                    self.top.append(flag)

        for key, _index in data.items():
            if key in self.flags:
                self.flags[key].index(_index)

    def get_data(self) -> Dict[str, int]:
        data = {}
        for name, flag in self.flags.items():
            data[name] = flag.get_index()
        return data

