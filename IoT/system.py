import sys
import json
import csv
from datetime import datetime as dt


class System:
    cards = []
    workers = []
    records = []
    terminals = []

    def __init__(self):
        """
        Constructor.
        Once System object was created read from Database (JSON files) initial information.
        """
        self.terminals = json.loads(open('resources/terminals.json', 'r').read())
        self.workers = json.loads(open('resources/workers.json', 'r').read())
        self.records = json.loads(open('resources/records.json', 'r').read())
        self.cards = json.loads(open('resources/cards.json', 'r').read())

    def loop(self):
        """
        Main system loop. Enter options on every iteration.

        :return: None
        """
        while True:
            for k, e in self.menu.items():
                print(f'{k} - {e[0]}')
            cmd = input(f'Choose command (1-{len(self.menu)}): ')
            print()
            if self.__check_input(cmd, range(1, len(self.menu) + 1)):
                self.menu.get(int(cmd))[1](self)

    def connect_terminal(self):
        """
        Creates new terminal and connect in to the system.

        :return: None
        """
        name = input('Enter terminal name to connect: ')
        if name != "" and name not in map(lambda e: e['name'], self.terminals):
            self.terminals.append({
                'id': len(self.terminals),
                'name': name
            })
            print(f'Terminal "{name}" was connected to the system.\n')
        else:
            print('Terminal with this name already exists or invalid input.\n')

    def disconnect_terminal(self):
        """
        Disconnects terminal from the system.

        :return: None
        """
        if self.__print_menu(self.terminals, '{KEY} - [ID_{id}] {name}', 'There is no any terminal to disconnect.\n'):
            key = input('Choose terminal to disconnect: ')
            if self.__check_input(key, range(len(self.terminals))):
                print('Terminal "%s" was disconnected from the system.\n' % self.terminals.pop(int(key))['name'])

    def pin_card_to_worker(self):
        """
        Pins card to worker choosing worker and then card.
        Update data in cards and workers lists.
        On menu shows only workers without cards.

        :return: None
        """
        without_cards = list(filter(lambda a: a['card_id'] == -1, self.workers))
        if self.__print_menu(without_cards, pattern='{KEY} - [ID_{id}] {name}'):
            key = input('Choose worker: ')
            if self.__check_input(key, range(len(without_cards))):
                worker = without_cards[int(key)]
                unused_cards = list(filter(lambda a: a['user_id'] == -1, self.cards))
                if self.__print_menu(unused_cards, '{KEY} - Card ID_{id}'):
                    key = input('Choose card: ')
                    if self.__check_input(key, range(len(unused_cards))):
                        card = unused_cards[int(key)]
                        self.workers[self.workers.index(worker)]['card_id'] = unused_cards[int(key)]['id']
                        self.cards[self.cards.index(card)]['user_id'] = worker['id']
                        print(f'Card {card["id"]} was pin to worker {worker["id"]}')

    def unpin_card_from_worker(self):
        """
        Unpin card from worker choosing only worker.
        Updates data in workers and cards lists.

        :return: None
        """
        with_cards = list(filter(lambda a: a['card_id'] != -1, self.workers))
        if self.__print_menu(with_cards, '{KEY} - [ID_{id}] {name}'):
            key = input('Choose worker: ')
            if self.__check_input(key, range(len(with_cards))):
                worker = with_cards[int(key)]
                card = list(filter(lambda e: e['id'] == worker['card_id'], self.cards))[0]
                self.workers[self.workers.index(worker)]['card_id'] = -1
                self.cards[self.cards.index(card)]['user_id'] = -1
                print(f'Card ID_{card["id"]} was unpinned from worker ID_{worker["id"]}\n')

    def generate_report(self):
        """
        Generates CSV file.

        :return: None
        """
        with open('report.csv', 'w', newline='') as f:
            wr = csv.DictWriter(f, fieldnames=self.records[0].keys())
            wr.writeheader()
            wr.writerows(self.records)

    def exit(self):
        """
        Use this method to stop program (system).
        Rewrites all modified lists of workers, terminals and etc in JSON files.

        :return: None
        """
        print('\nSee you!')
        open('resources/cards.json', 'w').write(json.dumps(self.cards))
        open('resources/records.json', 'w').write(json.dumps(self.records))
        open('resources/workers.json', 'w').write(json.dumps(self.workers))
        open('resources/terminals.json', 'w').write(json.dumps(self.terminals))
        sys.exit(0)

    def register_card(self):
        """
        Methods register card in terminal by choosing terminal and then card.
        After validation of user inputs method creates records to export.
        Writes to global list and then to JSON.

        :return: None
        """
        if self.__print_menu(self.terminals, '{KEY} - [ID_{id}] {name}'):
            key = input('Choose terminal: ')
            if self.__check_input(key, range(len(self.terminals))):
                terminal = self.terminals[int(key)]
                if self.__print_menu(self.cards, '{KEY} - Card ID_{id}'):
                    key = input('Choose card: ')
                    if self.__check_input(key, range(len(self.cards))):
                        card = self.cards[int(key)]
                        self.records.append({
                            'terminal_id': terminal['id'],
                            'card_id': card['id'],
                            'time': dt.now().strftime('%Y-%m-%d %H:%M:%S')
                        })
                        print('Record was added.')

    def add_card(self):
        """
        Adds new card to the system.

        :return: None
        """
        _id = input('Enter new card ID: ')
        if _id.isdigit() and int(_id) not in map(lambda e: e['id'], self.cards):
            self.cards.append({
                'id': int(_id),
                'user_id': -1
            })
            print(f'Card ID_"{_id}" was added to the system.\n')
        else:
            print('Card with such ID already exists or invalid input.\n')

    def remove_card(self):
        """
        Removes card from the system by ID.

        :return: None
        """
        if self.__print_menu(self.cards, '{KEY} - Card ID_{id}', 'There is no any card to remove.\n'):
            key = input('Choose card to remove: ')
            if self.__check_input(key, range(len(self.cards))):
                print('Card "%s" was removed from the system.\n' % self.cards.pop(int(key))['id'])

    @staticmethod
    def __print_menu(options, pattern, _string='List is empty.\n', cancel=True):
        """
        Additional method for easy printing any menus passing only a few params.
        Also you are able to use Cancel option.

        :param options: Items to print
        :param pattern: Formatted string for output
        :param _string: Optional string for invalid options
        :param cancel:  Optional var for Cancel option
        :return:        Boolean
        """
        if not options:
            print(_string)
            return False
        for i, option in enumerate(options):
            print(pattern.format(**option, KEY=i))
        print(f'{len(options)} - Cancel\n' if cancel else '')
        return True

    @staticmethod
    def __check_input(key, _range, _int=True, _cancel=True, _string='Invalid choice.'):
        """
        Checks input menu key for a few conditions. Returns true if passes all conditions.

        :param key:     Key, as element of menu
        :param _range:  Range in which key has to be
        :param _int:    Optional type of key
        :param _cancel: Optional bool for Cancel option in menus
        :param _string: Optional string for additional information
        :return:        Boolean or None depends on condition
        """
        if _int and key.isdigit():
            if int(key) in _range:
                return True
            else:
                print(_string if _cancel and int(key) != len(_range) else '', end='\n\n')
        else:
            print(_string)

    menu = {
        1: ('Connect RFID terminal', connect_terminal),
        2: ('Disconnect RFID terminal', disconnect_terminal),
        3: ('Add card to the sys', add_card),
        4: ('Remove card from the sys', remove_card),
        5: ('Pin card to worker', pin_card_to_worker),
        6: ('Unpin card from worker', unpin_card_from_worker),
        7: ('Register card', register_card),
        8: ('Generate report', generate_report),
        9: ('Exit and save', exit)
    }
    """
    Menu items based on System class functions.
    Use dictionary to easy access name and value (func).
    """
