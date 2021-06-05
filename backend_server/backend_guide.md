This is for newbies who want to contribute in the back end of this project.
## APIs for hemontika
Here are the APIs for connecting the backend with front end -
### `api/novels/`
It gives all the novel model objects.The outcome is given below -
```json
[
    {
        "id": 1,
        "title": "A novel NOT about testing",
        "author": 1,
        "front_img": "http://127.0.0.1:8000/front_img.png",
        "date": self.DATE,
        "tags": [
            1,
        ],
        "number_of_chapters": 2
    },
    {
        "id": 2,
        "title": "Another novel",
        "author": 2,
        "front_img": null,
        "date": self.DATE,
        "tags": [],
        "number_of_chapters": 3
    }
]
```
### `api/poems/`
same as above. Gives the list of poem model objects. Example -
```json
[
    {
        "id": 1,
        "title": "blossoms",
        "author": 1,
        "front_img": null,
        "date": self.DATE,
        "tags": [
            1,
        ]
    },
    {
        "id": 2,
        "title": "two blossoms",
        "author": 2,
        "front_img": null,
        "date": self.DATE,
        "tags": []
    },
    {
        "id": 3,
        "title": "three blossoms",
        "author": 2,
        "front_img": null,
        "date": self.DATE,
        "tags": []
    }
]
```
### `api/stories/`
Gives a list of existing Stories. Example -
```json
[
    {
        "id": 1,
        "title": "a story about serializer",
        "author": 1,
        "front_img": null,
        "date": self.DATE,
        "tags": [
            1,
            2,
            3
        ]
    },
    {
        "id": 2,
        "title": "title",
        "author": 1,
        "front_img": null,
        "date": self.DATE,
        "tags": [
            1
        ]
    }
]
```

### `api/books/`
Gives a list of all books. Format -
```json
[
    {
        "id": 1,
        "title": " a book about testing",
        "author": 1,
        "front_img": null,
        "number_of_contents": 4,
        "date": self.DATE,
        "tags": []
    }
]
```
### `api/tags/`
It gives all the tags that currently exist in the database.Output format -
```json
[
    {
        "id": 1,
        "name": "horror",
    },
    {"id": 2, "name": "mystry"},
    {"id": 3, "name": "fiction"},
    {"id": 4, "name": "crime"}
]
```
### `api/novels/<int:pk>/`  (under development)
Gives a specific novel matching the queried id. Example output will be shared soon.

### `api/stories/<int:pk>/` (under development)
Gives a specific story with the matching id defined on the url.
### `api/poems/<int:pk>/` (under development)
Gives a specific poem that matches with the id specified in the url.
### `api/books/<int:pk>/` (under development)
Gives a specific book with the specified id.
### `api/tags/<int:pk>/`
Gives a specific tag based on the id specified on the url. Example -
`{"id": 1, "name": "horror", "poems": [], "novels": [], "stories": [], "books": []}`

**Note: More api url will be avaialable soon**