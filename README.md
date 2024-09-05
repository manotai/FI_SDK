# Feedback Intelligence SDK

The `feedbackIntelligenceSDK` is a Python package designed to interact with the Feedback Intelligence API. It allows you
to add context, chat, and feedback data to the database, both synchronously and asynchronously.

## Installation

You can install the package via pip:

```bash
pip install feedbackIntelligence
```

Usage
Initialization
To use the SDK, first initialize it with your API key:

```python
from feedbackIntelligence.fi import FeedbackIntelligenceSDK

sdk = FeedbackIntelligenceSDK(api_key="your_api_key_here")
```

## Methods

- ***add_context***

#### Add context to the database (synchronous)

```python
response = sdk.add_context( project_id=1, context="Sample context", context_id=123)
# Or you can skip the context_id
#response = sdk.add_context( project_id=1, context="Sample context")

```

- ***add_context_async***

#### Add context to the database (asynchronous)

```python
response = await sdk.add_context_async( project_id=1, context="Sample context", context_id=123)
```

- ***add_chat***

#### Add chat data to the database (synchronous).

```python
from feedbackIntelligence.schemas import Message, Context, Feedback
# Make sure to use the exact date format that is used in the example

messages = [
    Message(role='human', text='Hello', propmt='test', 
            date='2020-01-20T13:00:00',
            context=Context(text='new_context')), 
    Message(role='ai', text='Hi there', 
            date='2020-01-20T13:01:00',
            feedback=Feedback(thumbs_up=1, message='Feedback message(optional)'))]
response = sdk.add_chat( project_id=1, chat_id=456, messages=messages)
```

- ***add_chat_async***

#### Add chat data to the database (asynchronous).

```python

response = await sdk.add_chat_async( project_id=1, chat_id=456, messages=messages)
```

- ***add_feedback***

#### Add feedback data to the database (synchronous).

```python
response = sdk.add_feedback( project_id=1, message="Great service", source="email")
```

- ***add_feedback_async***

#### Add feedback data to the database (asynchronous).

```python
response = await sdk.add_feedback_async( project_id=1, message="Great service", source="survey")
```

visit this links to see examples
* [SKD](https://colab.research.google.com/drive/1p6ZkAj0zQoKtlv4FETE5Mrb4PXn-IhuA?usp=drive_link)
* [API](https://drive.google.com/file/d/1cwjbqVIAFidlbhYv8YA36P6PDhpufT9c/view?usp=drive_link)
