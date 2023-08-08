from abc import ABC, abstractmethod
import json


# Base adapter class implementing the common conversion logic
class Transformer:
    @abstractmethod
    def convert(self, data):
        # Adapter method for conversion
        pass


# Data classes
class JSON(str):
    pass


class XML(str):
    pass


class Proto(str):
    pass


# Adapter classes
class JsonToXmlAdapter(Transformer):
    def convert(self, data: JSON) -> XML:
        """
        Converts JSON data to XML format using a specific conversion logic.
        """
        return XML("<xml>{}</xml>".format(data))


class XmlToJsonAdapter(Transformer):
    def convert(self, data: XML) -> JSON:
        """
        Converts XML data to JSON format using a specific conversion logic.
        """
        # Logic to convert XML data to JSON
        return JSON(json.dumps({"xml_data": str(data)}))


class ProtoToXmlAdapter(Transformer):
    def convert(self, data: Proto) -> XML:
        """
        Converts Proto data to XML format using a specific conversion logic.
        """
        return XML("<xml>{}</xml>".format(data))


# Client class utilizing the adapter pattern
class Client:
    def __init__(self, transformer: Transformer) -> None:
        """
        Initializes the client with a specific adapter.
        """
        self.transformer = transformer

    def convert(self, data) -> object:
        """
        Uses the adapter to convert data based on the adapter type.
        """
        return self.transformer.convert(data)


def main():
    # Usage
    json_to_xml_adapter = JsonToXmlAdapter()
    client1 = Client(json_to_xml_adapter)
    json_data = JSON('{"key": "value"}')
    xml_data = client1.convert(json_data)
    print("JSON to XML Data:", xml_data)

    xml_to_json_adapter = XmlToJsonAdapter()
    client2 = Client(xml_to_json_adapter)
    xml_data = XML('<xml><key>value</key></xml>')
    json_data = client2.convert(xml_data)
    print("XML to JSON Data:", json_data)

    proto_to_xml_adapter = ProtoToXmlAdapter()
    client3 = Client(proto_to_xml_adapter)
    proto_data = Proto('proto-data')
    xml_data = client3.convert(proto_data)
    print("Proto to XML Data:", xml_data)


if __name__ == '__main__':
    main()
