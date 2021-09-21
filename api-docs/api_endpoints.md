# Possible required endpoints for frontend


## **/profile/{{profileId}}/**
Expected Response Body: 
```json
{
    "profilePic": "url",
    "username": "john",
    "firstName": "John",
    "lastName": "Doe",
    "age": "23",
    "country": "Unknown",
    "city": "City",
    "publishedPoems": "24",
    "publishedStories": "45", 
    "publishedBooks": "45", 
    "publishedNovels": "45", 
}
```

## **/literature/categories/stories/**
Expected Response Body:
```json
[
    {
        "thumbnailPic": "url",
        "title": "Title",
        "rating": "4.3",
        "category": "Category",
        "readTime": "6 min"
    }
]
```

## **/literature/categories/poems/**
```json
[
    {
        "thumbnailPic": "url",
        "title": "Title",
        "rating": "4.3",
        "category": "Category",
        "readTime": "6 min"
    }
]
```

## **/literature/categories/novels/**
```json
[
    {
        "thumbnailPic": "url",
        "title": "Title",
        "rating": "4.3",
        "category": "Category",
        "noOfChapters": "20"
    }
]
```

## **/paintings/**
```json
    // Incomplete
```
## **/musics/**
```json
    // Incomplete
```
## **/recitations/**
```json
    // Incomplete
```

## **/stories/{{storyId}}/details/**
```json
{
    "thumbnailPic": "url",
    "title": "Title",
    "author": {
        "name": "Author", //It can be pseudo-name or full name or even empty string
        "username": "username" //This is must
    },
    "rating": "4.3",
    "readTime": "6min",
    "views": "1232342",
    "publishedOn": "UTC time",
    "category": "Category",
    "tags": [{ "id": "ID", "name": "Tag" }],
    "description": "Description",
    "downloadURL": "URL"
}
```

## **/stories/{{storyId}}/comments/**
```json
[
    {
        "id": "commentid",
        "user": {
            "name": "PseudoName | Full Name | Empty String", // Depending on user's settings
            "username": "username"
        },
        "commentedOn": "UTC Date",
        "content": "Comment",
        "likes": "34",
        "replies": "45"
    }
]
```

## **/stories/{{storyid}}/comments/{{commentId}}/replies**
```json
// Same as Comments
```

## **/users/{{userId}}/incomplete-literatures/**
```json
[
    {
        "id": "SomeId",
        "title": "Title",
        "type": "Novel"
        // Incomplete
    }
]
```