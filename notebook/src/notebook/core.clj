(ns notebook.core
  (:gen-class)
  (:require notebook.join-md
            notebook.md-link-tree
            notebook.pick-code))

(def tools (array-map 
            :pick-code notebook.pick-code/run
            :link-tree notebook.md-link-tree/run
            :join-md notebook.join-md/run))

(defn- do-with-log [name consumer]
  (println "Do" name)
  (consumer)
  (println "Done" name))

(defn -main 
  "pick-code: picks Python code
   link-tree: makes link tree on Markdown
   join-md:   joins Markdown files into index.md"
  [& args]
  (cond 
    (empty? args)
    (println "No command.")

    (= "all" (first args))
    (doseq [tool tools]
      (let [[k v] tool]
        (do-with-log (name k) v)))

    (every? #(tools (keyword %)) args)
    (doseq [arg args]
      (let [tool (-> arg
                     keyword
                     tools)]
        (do-with-log arg tool)))

    :else
    (println "Invalid arguments.")))
