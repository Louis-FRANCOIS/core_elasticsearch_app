""" Autocomplete settings for the data collection
"""

# settings for CDCS data
DATA_AUTOCOMPLETE_SETTINGS = {
    "settings": {
        "analysis": {
            "filter": {
                "autocomplete_filter": {
                    "type": "edge_ngram",
                    "min_gram": 1,
                    "max_gram": 20,
                }
            },
            "analyzer": {
                "autocomplete": {
                    "type": "custom",
                    "tokenizer": "standard",
                    "filter": ["lowercase", "autocomplete_filter"],
                }
            },
        }
    },
    "mappings": {
        "properties": {
            "title": {
                "type": "text",
                "analyzer": "autocomplete",
                "search_analyzer": "standard",
            },
            "description": {
                "type": "text",
                "analyzer": "autocomplete",
                "search_analyzer": "standard",
            },
        }
    },
}
