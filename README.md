
cps-flask
=========

- setup environment

```sh
> mkvirtualenv env
> pip install -r requirements.txt
```

- run server on port 8000 for debugging

```sh
python cps.py -p 8000 -d
```

- or test db

```sh
## will create a test.db file
python testdb.py
```

# Database

## 多語支援
以下斜體字的table就是有多語支援
多語支援的table名稱會post-fixed by `_en` 或 `_zh`

## News 新聞

### news
| id (integer)  | image_url (string)  | publish_time (unix timestamp)|
|:------------- |:---------------:| -------------:|
| 1     | http://xxx.yyy.xxx/mmm.jpg | 1402342345 |


### *news_description*
| id (integer)  | description (string) |
|:------------- |:---------------:|
| 1     | 新手機上市 |



### *news_content*
| id (integer)  | content (string) |
|:------------- |:---------------:|
| 1     | \<div>新手機上市\</div> |

### *news_title*
| id (integer)  | title (string) |
|:------------- |:---------------:|
| 1     | 手機新知 |


## Product 商品

### product
| id (integer)  | image_url (string)  | publish_time (unix timestamp)| product_type (enum) | related_product(string) | brand (enum) |
|:------------- |:---------------:| -------------:| -------------:| -------------:| -------------:|
| 1     | http://xxx.yyy.xxx/mmm.jpg | 1402342345 | 2 | (23,44,53,25) | 3 |

### Brand
| id (integer)  | name (string)  |
|:------------- |:---------------:|
| 1     | 鴻海 |
| 2     | Nokia |


### *prodcut_type*
| id (integer)  | name (string)  |
|:------------- |:---------------:|
| 1     | 商品 |
| 2     | 配件 |


### *product_content*
| id (integer)  | content (string) |
|:------------- |:---------------:|
| 1     | \<li>32G Rom\</li>\<li>Intel Atom\</li> |



### *product\_title*
| id (integer)  | title (string) |
|:------------- |:---------------:|
| 1     | Nokia 3310 |



