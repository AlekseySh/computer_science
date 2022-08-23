import Data.Char

data Entry k1 k2 v = Entry (k1, k2) v  deriving Show

data Map k1 k2 v = Map [Entry k1 k2 v]  deriving Show


instance Functor (Entry k1 k2) where
    fmap f (Entry (k1, k2) v) = Entry (k1, k2) (f v) 

instance Functor (Map k1 k2) where
    fmap f (Map xs) = Map (map (fmap f) xs)



test0 = fmap (map toUpper) $ Map []
test1 = fmap (map toUpper) $ Map [Entry (0, 0) "origin", Entry (800, 0) "right corner"]



------------------------------------------


data Log a = Log [String] a deriving Show

bindLog :: Log a -> (a -> Log b) -> Log b
bindLog (Log log0 x0) f = Log (concat [log0, [m1]]) x1
    where
        Log [m1] x1 = f x0


toLogger :: (a -> b) -> String -> (a -> Log b)
toLogger f msg x = Log [msg] (f x)


add1Log = toLogger (+1) "added one"
mult2Log = toLogger (* 2) "multiplied by 2"

test2 = Log ["nothing done yet"] 0 `bindLog` add1Log
test3 = Log ["nothing done yet"] 3 `bindLog` add1Log `bindLog` mult2Log

test4 = Log [] 0 `bindLog` add1Log


execLoggersList :: a -> [a -> Log a] -> Log a
execLoggersList x fs   = execLoggersList' x (reverse fs)

execLoggersList' x []        = Log [] x
execLoggersList' x (f:ftail) = (execLoggersList' x ftail) `bindLog` f

test5 = execLoggersList 3 [add1Log, mult2Log, \x -> Log ["multiplied by 100"] (x * 100)]



data Token = Number Int | Plus | Minus | LeftBrace | RightBrace 
    deriving (Eq, Show)

asToken :: String -> Maybe Token
asToken s
    | all isDigit s  = Just (Number (read s :: Int))
    | s == "+"       = Just Plus
    | s == "-"       = Just Minus
    | s == "("       = Just LeftBrace
    | s == ")"       = Just RightBrace
    | otherwise      = Nothing


tokenize :: String -> Maybe [Token]
tokenize = sequence . map (asToken) . words

test6 = tokenize "1 + ( 7 - 2 )"




data Board = Board Int deriving Show

nextPositions :: Board -> [Board]
nextPositions (Board i) = [Board (i + 1), Board (i + 2)]

nextPositionsN :: Board -> Int -> (Board -> Bool) -> [Board]
nextPositionsN b n predicat
    | n < 0     = []
    | otherwise = filter predicat (nextPositionsN' b n predicat)
    
nextPositionsN' b 0 predicat = [b]
nextPositionsN' b n predicat = concatMap nextPositions (nextPositionsN' b (n - 1) predicat)


test7 n = nextPositionsN (Board 1) n (\(Board i) -> odd i)



