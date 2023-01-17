def format_table():
    with open('data.csv','r') as file:
        lines = file.readlines()
    
    html = ""
    data = []
    for line in lines:
        data.append(line.split(','))
    
    html += "<table> <thead>"
    html += f"""
    <tr> 
        <th> {data[0][0]} </th>
        <th> {data[0][1]} </th>
        <th> {data[0][2]} </th>
        <th> {data[0][3]} </th>
        <th> {data[0][4]} </th>
    </tr>
    """
    for i in range(1, len(data)):

        html += f"""
            <tr>
            <td> {data[i][0]} </td>
            <td> {data[i][1]} </td>
            <td> {data[i][2]} </td>
            <td> {data[i][3]} </td>
            <td> {data[i][4]} </td>
            </tr>
        """

    html += "</thead> </table>"
    return html
     
print(format_table())