## How would you make asim search work ##

### Need to create embeddings ###

1. Model to use: indicBert
2. Tokenize the book to paragraph level embeddings
3. Have a good datastructure to reference the Book, page and topic name


### Books??? ###

Need a translation layer from a mobi version to a Book Data Structure

For Simplicity we'll only have the main text i.e. not including uppodghat, samarpan and sampadakya. 



Book : 


A book is generally organised like the following schema.

```
    name: str
    khands:
        [
            {
                khand_number: int
                khand_title: str 
                chapters: {
                    [
                    chapter_number: int
                    chapter_title: str
                    topics: {
                        [
                            {
                                topic_title: str
                                starting_pg: int
                                paras: [
                                    {
                                        para_str: string #(regular guj string),
                                        para_guid: guid,
                                        para_embedding
                                    },
                                    .
                                    .
                                    .

                                ]
                            },
                            .
                            .
                            .
                        ]
                    },
                    .
                    .
                    .
                    ]
                }
            }     
        ]

```

para_topic embedding like mongo would work better.

Actually we do not need a whole schema like above. We just need two collections and a good relation between them.

Collection 1 being the paragraph:

Paragraph:

```
{
    paragraph_str: str (regular gujarati string),
    paragraph_guid: guid,
    paragraph_seq_number: int, #This is just sad, need to think  more
    paragraph_embedding: VECTOR generated by IndicBert
    topic_id: guid <Ref Metadata table>
}
```

```
Topics:
{
    topic_id: guid    
    chapter_name:
    topic_name:    
}
```

val.title = topic_name or chapter_name

when it is topic name:
topic.name = val.title
topic.chapter_name = running chapter

when it is chapter name
