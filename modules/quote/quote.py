# Morphux-IRC-BOT
# Quote save system
# By Noich
import  time
import  json
import sys
# sys.setdefaultencoding() does not exist, here!


class Quote:
    def command(self):
        self.config = {
                "command": {
                        "quote": {
                                "function": self.fetchQuote,
                                "usage": "quote [number]",
                                "help": "fetches a quote from previously saved quotes"
                        },
                        "savequote": {
                                "function": self.saveQuote,
                                "usage": "savequote #author [quote]",
                                "help": "saves a quote with its author"
                        },
                        "qsearch": {
                                "function": self.searchQuote,
                                "usage": "qsearch [args]",
                                "help": "searches a quote based on given args"
                        }
                }
        }
        with open ("/morphux/Morphux-IRC-Bot/modules/quote/quote.json", "r") as myfile:
            data=myfile.read().replace('\n', '')
        data = data.replace("\\\"", "'")
        string = data#.decode('unicode_escape')
        self.quoteList = json.loads(string)
        self.quote = [None, None, None]
        return self.config

    def fetchQuote(self, Morphux, infos):
        if (len(infos['args']) == 0):
            Morphux.sendMessage("I have " + str(len(self.quoteList))  +" quotes available. Choose one", infos['nick']);
        elif (infos['args'][0].isdigit() == False):
            Morphux.sendMessage("No such quote - Nice Try!", infos['nick']);
        elif (int(infos['args'][0]) < len(self.quoteList)):
            Morphux.sendMessage("Quote #" + infos['args'][0] + ", By: " + str(self.quoteList[int(infos['args'][0])][1]) + ", " + str(self.quoteList[int(infos['args'][0])][0]), infos['nick']);
            self.quoteList[int(infos['args'][0])][2] = self.quoteList[int(infos['args'][0])][2]

            Morphux.sendMessage(self.quoteList[int(infos['args'][0])][2]);
        else:
            Morphux.sendMessage("No such quote - Nice Try!", infos['nick']);

    def saveQuote(self, Morphux, infos):
        if (len(infos['args']) == 0):
            Morphux.sendMessage("I dont have anything to save, cmon!", infos['nick']);
        else:
            if (infos['args'][0] == ""):
                Morphux.sendMessage("OMG BUG");
            elif (infos['args'][0][0] != '#'):
                Morphux.sendMessage("Your first argument is supposed to be #author. God you're stupid.", infos['nick']);
            else:
                self.quote = [None, None, None];
                i = 0
                self.quote[0] = time.strftime("%d/%m/%Y")
                self.quote[1] = str(infos['args'][0][1:])
                for arg in infos['args']:
                    if (i > 0):
                        if self.quote[2] is None:
                            self.quote[2] = str(arg);
                        else:
                            self.quote[2] += str(' ')
                            self.quote[2] += str(arg);
                    else:
                        i = 1;
                self.quoteList[len(self.quoteList):] = [self.quote]
                with open('modules/quote/quote.json', 'w') as f:
                    json.dump(self.quoteList, f);
                f.close()
                Morphux.sendMessage("Quote saved as #" + str(len(self.quoteList) - 1), infos['nick'])

    def searchQuote(self, Morphux, infos):
        if (len(infos['args']) == 0):
            Morphux.sendMessage("Need a keyword", infos['nick']);
        else:
            i = 0
            result = ""
			for i in range(1, len(self.quoteList):
                if (infos['args'][0] in self.quoteList[i][2]):
                    result = result + str(i) + ", "
            if (result == ""):
                Morphux.sendMessage("No quote found.", infos['nick']);
            else:
                Morphux.sendMessage("Quote(s) found: " + result[:-2], infos['nick']);
	def searchAuthor(self, Morphux, infos):
        if (len(infos['args']) == 0):
            Morphux.sendMessage("Need an author", infos['nick']);
		else:
			i = 0;
			result = ""
			author = infos['args'][0].tolower()
			for i in range(1, len(self.quoteList):
				if author in self.quoteList[i][1]:
					result += str(i) + ", "
            if (result == ""):
                Morphux.sendMessage("No quote found for {}.".format(infos['args'][0]), infos['nick']);
            else:
                Morphux.sendMessage("Quote(s) found: " + result[:-2], infos['nick']);
