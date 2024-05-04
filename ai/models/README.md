Some info about models naming:\
X.json - dataset example\
X.keras - simpliest model, output 1 number, negative = neutral message, positive = redflag\
X-new.keras - output 2 numbers, probably for "neutral" and "redflag" messages\
checkpoint - model weights, use when can't load .keras model\

Guide to training own model:
1. Prepare dataset. Dataset is two categories of messages, 0 = neutral messages with no redflags, 1 = messages of target people with redflags
2. Store dataset as JSON like this:\
{\
  "0": [ "msg1", "msg2"... ],\
  "1": [ "msg1", "msg2"... ]\
}
3. Call train_model from train.py with path to dataset and path to output model