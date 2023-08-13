# LunaFlashy

Python Project

Method:
python/ http/ json/ api

Basic Function:

1. Search word from dictionary, display them.
2. Prounciate the word.
3. add words in local database.
4. edit words in local database.
5. delete words in local database.
6. search words in local database, count how many times this word has been inquired.

Advanced function:

1. flashcard test

version 1.0.0 @11/21/2022:

1. new api: https://dictionaryapi.dev/
2. save history
3. text wrap ==> removed. useless feature.
4. download audio file

version 1.0.1 @11/27/2022:

1. changed api => https://dictionaryapi.com/products/json
   1.1 [Feature1] idioms. syns(RegEx).
   1.2 [Feature2] smart-spell: if there is misspelling, it will suggest alternatives.
   1.3 [Bug] Fixed Input error, convert to all lowercase.
   1.4 [Feature] It can provide more than one audioes, but I can bring the words with them yet, just keep one.
   1.5 [Bug] Fixed audio error, using RegEx to make sure there is audio available
   1.6 [Bug] Fixed phonetic display error, using codecs.decode(str,'unicode_escape') to convert raw string into normal string.
2. OS
   2.1 [Feature3] be able to delete items and data on local disk.
   2.2 [Feature4] be able to review items and the number of them.
   2.3 [Reliability1] local documents
3. [Portability1] designed in OOP
4. Git

version 1.0.2 @????:

1. [Maintainability1] testing - bug record.
2. [Efficiency1] Data Structure[hash map].
   2.1 [Bug1] Api-json: for every part of speech, make a list to store their definition. (eg. practical)
   2.2 [Bug2] Api-json: remove the duplicate definition.
3. OS
   4.1 [Reliability2] retrive from local files[no api].
   4.2 [Reliability3] auto synchronize, make sure files correct.
   4.3 [Feature5] allow users to add tags for it.
   4.4 [Feature6] add how many times being inquiried in json.
   4.5 [Fearure7] do you want to review???[try yield???] => print out every entry one by one and show the meaning after cmd, then decide to change the proficient rate. algo: correct time/ inquiry time
   learn more about python parsing json document.. deal with data..
4. [Scalability]Website Design
   5.1 [SkillsStack1] html/css
   5.2 [SkillsStack2] javascript

version 1.1.0 @????:

1. More Functions...
   1.1 This is just a personal study tool. I gotta think more functions to bring it on the web.
   1.2 Not only dictionary..maybe leetcode or any subject???
   1.3 Need to explore more practicle features:
   1.3.1 [Feature]test: definitions with multi-selected options.
   1.3.2 [Feature]every day send to my inbox.
   1.3.3 [Feature]test: spell with audio and phonetic.
2. OOP Design
   2.1 [Portability] be more logical in OOP.
3. Learn more about software architecture.
