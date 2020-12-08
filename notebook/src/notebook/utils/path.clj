(ns notebook.utils.path
  (:require [clojure.java.io :as io]))

(def windows-os? (clojure.string/includes? (System/getProperty "os.name") "Windows"))

(def base "../doc")
(def base-re (if windows-os? #"\.\.\\doc" #"\.\./doc"))

(defn has-extension? [path extension]
  (boolean
   (re-find (re-pattern (str "\\." extension "$")) 
            (.toString path))))

(defn path-seq [path]
  (map #(.toString %) (iterator-seq (.iterator path))))

(defn files [base extension]
  (->> base
       io/file
       file-seq
       (filter #(has-extension? % extension))))
