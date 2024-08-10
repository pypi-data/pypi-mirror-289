# AO3 Parser
Tools for parsing AO3 pages and creating urls based on requirements.

Main advantage over similar packages is it's complete control over requests to AO3.
Instead of handling requests on it's own, it shifts this to the user, giving more room for optimization.
The main bottleneck for anyone in need of collecting larger amounts of data.
(Scraping data for AI training is discouraged)

If this is not what you're looking for, I'd recommend [ao3_api](https://github.com/ArmindoFlores/ao3_api) that handles requests on it's own.

## Installation
```bash
pip install ao3-parser
```

# Usage
An average user will find themselves using two main modules the most, `Search` and `Page`. 

## Search
Common example of using `Search` would look like this.
Just like on AO3, pages are numbered from 1 and up.

```python
import AO3Parser as AO3P
from AO3Parser import Params
from datetime import datetime

search = AO3P.Search("Original Work", Sort_by=Params.Sort.Kudos,
                     Include_Ratings=[Params.Rating.General_Audiences],
                     Words_Count="1000-1500",
                     Date_From=datetime(2024, 6, 30))
url = search.GetUrl(page=1)
print(f"URL: {url}")
```
```
URL: https://archiveofourown.org/works?commit=Sort+and+Filter&page=1&work_search%5Bsort_column%5D=kudos_count&tag_id=Original+Work&include_work_search%5Brating_ids%5D%5B%5D=10&work_search%5Bword_count%5D=1000-1500&work_search%5Bdate_from%5D=2024-06-30
```

The `Words_Count`, `Hits_Count`, `Kudos_Count`, `Comments_Count` and `Bookmarks_Count` parameters are string types that use AO3 type formatting.
> #### Work Search: Numerical Values
> Use the following guidelines when looking for works with a specific amount of words, hits, kudos, comments, or bookmarks. Note that periods and commas are ignored: 1.000 = 1,000 = 1000.
>
>> `10`:  
>> a single number will find works with that exact amount  
> 
>> `<100`:  
>> will find works with less than that amount 
> 
>> `>100`:  
>> will find works with more than that amount  
> 
>> `100-1000`:  
>> will find works in the range of 100 to 1000

## Page

```python
import AO3Parser as AO3P
import requests

search = AO3P.Search("Original Work")
url = search.GetUrl()
page_data = requests.get(url).content

page = AO3P.Page(page_data)
print(f"Total works: {page.Total_Works}")
print(f"Works on page: {len(page.Works)}")
print(f"Title of the first work: [{page.Works[0].Title}]")
```
```
Total works: 282069
Works on page: 20
Title of the first work: [Title Of This Work]
```

## Work
All data that is parsed from a page into works can be seen below.
```python
ID: int
Title: str
Authors: list[str]
Fandom: list[str]
Summary: str

Language: str
Words: int
Chapters: int
Expected_Chapters: int
Comments: int
Kudos: int
Bookmarks: int
Hits: int
UpdateDate: datetime

Rating: Params.Rating
Categories: list[Params.Category]
Warnings: list[Params.Warning]
Completed: bool

Relationships: list[str]
Characters: list[str]
Additional_Tags: list[str]
```
`Summary`, `Words`, `Expected_Chapters`, `Comments`, `Kudos`, `Bookmarks` and `Hits` are set to `None` if not specified on a page.
### Notes
`Params.Category.No_Category` is not recognized as a valid ID on AO3 and should not be used with `Search`.