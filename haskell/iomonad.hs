import System.Directory
import System.IO
import Data.List
import System.FilePath

main' :: IO ()
main' = do
    
    putStr "Substring: "
    hFlush stdout
    sub <- getLine

    files <- getDirectoryContents "."

    if null sub then putStrLn "Canceled" else mapM_ (\x -> if (isInfixOf sub x) then (putStrLn ("Removing file: " ++ x)) else putStr "") files

    putStrLn ""

main = main'
