import os

def refresh_logger(filename):
    """Remove old logs and create new ones."""
    if os.path.isfile(filename):
        try:
            os.remove(filename)
        except Exception:
            pass
    open(filename, 'a').close()

    

def decodeBlock(block):
    """
    Decode various pieces of info for a block import all and return the parsed data
    """

    try:
        b = block

        new_block = {
            "number": b["number"],
            "timestamp": b["timestamp"],
            "transactions": []
        }

        #Filter and decode each tx
        #Value, gas, and gasPrice are all converted tp ether
        for t in b["transactions"]:
            new_t = {
                "from": t["from"],
                "to": t["to"],
                "value": t["value"]/1000000000000000000.,
                "data": t["input"]
            }
            new_block["transactions"].append(new_t)
        return new_block

    except:
        return None