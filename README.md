# Setup
To start the project open the console, cd into root dir and run 
```./run.sh```
Once the project has started, in another console window run
```./run.sh manage migrate api```


# Test
Example table POST & PUT data:
```
{
   "name":"mytable",
   "fields": [
      {
         "name":"columnstr",
         "type":"string"
      },
      {
         "name":"columnnr",
         "type":"number"
      },
      {
         "name":"columnbool",
         "type":"boolean"
      }
   ]
}
```

Example row PUT data:
```
{
   "columnstr":"tst",
   "columnnr": 123,
   "columnbool": 123
}
```