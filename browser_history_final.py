import pandas as pd
import browser_history
import os

def hist_Firefox():
    from browser_history.browsers import Firefox
    f= Firefox()
    outputs = f.fetch_history()
    his = outputs.histories
    df = pd.DataFrame(his, columns=['DateTime', 'URL'])

    df.sort_values(by='DateTime', inplace=True)

    csv_filename = os.path.join(current_directory, 'Firefox.csv')
    df.to_csv(csv_filename, index=False)

def hist_Chrome():
    from browser_history.browsers import Chrome
    f= Chrome()
    outputs = f.fetch_history()
    his = outputs.histories
    df = pd.DataFrame(his, columns=['DateTime', 'URL'])

    df.sort_values(by='DateTime', inplace=True)

    csv_filename = os.path.join(current_directory, 'Chrome.csv')
    df.to_csv(csv_filename, index=False)

def hist_Brave():
    from browser_history.browsers import Brave
    f= Brave()
    outputs = f.fetch_history()
    his = outputs.histories
    df = pd.DataFrame(his, columns=['DateTime', 'URL'])

    df.sort_values(by='DateTime', inplace=True)

    csv_filename = os.path.join(current_directory, 'Brave.csv')
    df.to_csv(csv_filename, index=False)


def hist_Opera():
    from browser_history.browsers import Opera
    f= Opera()
    outputs = f.fetch_history()
    his = outputs.histories
    df = pd.DataFrame(his, columns=['DateTime', 'URL'])

    df.sort_values(by='DateTime', inplace=True)

    csv_filename = os.path.join(current_directory, 'Opera.csv')
    df.to_csv(csv_filename, index=False)

def hist_Safari():
    from browser_history.browsers import Safari
    f= Safari()
    outputs = f.fetch_history()
    his = outputs.histories
    df = pd.DataFrame(his, columns=['DateTime', 'URL'])

    df.sort_values(by='DateTime', inplace=True)

    csv_filename = os.path.join(current_directory, 'Safari.csv')
    df.to_csv(csv_filename, index=False)

def hist_Chromium():
    from browser_history.browsers import Chromium
    f= Chromium()
    outputs = f.fetch_history()
    his = outputs.histories
    df = pd.DataFrame(his, columns=['DateTime', 'URL'])

    df.sort_values(by='DateTime', inplace=True)

    csv_filename = os.path.join(current_directory, 'Chromium.csv')
    df.to_csv(csv_filename, index=False)

def hist_edge():
    from browser_history.browsers import Edge
    f= Edge()
    outputs = f.fetch_history()
    his = outputs.histories
    df = pd.DataFrame(his, columns=['DateTime', 'URL'])

    df.sort_values(by='DateTime', inplace=True)

    csv_filename = os.path.join(current_directory, 'Edge.csv')
    df.to_csv(csv_filename, index=False)

def hist_LibreWolf():
    from browser_history.browsers import LibreWolf
    f= LibreWolf()
    outputs = f.fetch_history()
    his = outputs.histories
    df = pd.DataFrame(his, columns=['DateTime', 'URL'])

    df.sort_values(by='DateTime', inplace=True)

    csv_filename = os.path.join(current_directory, 'LibreWolf.csv')
    df.to_csv(csv_filename, index=False)

def hist_OperaGX():
    from browser_history.browsers import OperaGX
    f= OperaGX()
    outputs = f.fetch_history()
    his = outputs.histories
    df = pd.DataFrame(his, columns=['DateTime', 'URL'])

    df.sort_values(by='DateTime', inplace=True)

    csv_filename = os.path.join(current_directory, 'OperaGX.csv')
    df.to_csv(csv_filename, index=False)

def hist_Vivaldi():
    from browser_history.browsers import Vivaldi
    f= Vivaldi()
    outputs = f.fetch_history()
    his = outputs.histories
    df = pd.DataFrame(his, columns=['DateTime', 'URL'])

    df.sort_values(by='DateTime', inplace=True)

    csv_filename = os.path.join(current_directory, 'Vivaldi.csv')
    df.to_csv(csv_filename, index=False)

if __name__ == "__main__":
    current_directory = os.getcwd()
    hist_Firefox()
    hist_Chrome()
    hist_Brave()
    hist_Opera()
    #hist_Safari()
    hist_Chromium()
    hist_edge()
    hist_LibreWolf()
    hist_OperaGX()
    hist_Vivaldi()