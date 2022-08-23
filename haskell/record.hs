import Data.Time.Clock
import Data.Time.Format

timeToString :: UTCTime -> String
timeToString = formatTime defaultTimeLocale "%a %d %T"

data LogLevel = Error | Warning | Info deriving Show

data LogEntry = LogEntry {timestamp :: UTCTime, logLevel :: LogLevel, message :: String}

logLevelToString :: LogLevel -> String
logLevelToString = show

logEntryToString :: LogEntry -> String
logEntryToString (LogEntry timestamp logLevel message) = (timeToString timestamp) ++ ": " ++ (show logLevel) ++ ": " ++ message


test1 =
  let ct = read "2019-02-24 18:28:52.607875 UTC"::UTCTime
      le = LogEntry ct Info "Info Message"
  in logEntryToString le



data Shape = Circle Double | Rectangle Double Double

isRectangle :: Shape -> Bool
isRectangle Rectangle{} = True
isRectangle _ = False




data Person = Person { firstName :: String, lastName :: String, age :: Int } deriving Show

abbrFirstName :: Person -> Person
abbrFirstName p = if length fn > 2 then p {firstName = take 1 fn ++ "."} else p
    where fn = firstName p




