require 'json'

module Jekyll

  class JSONPost < Page; end

  class JSONGenerator < Generator
    priority :lowest
    safe true

    # Generates an individual JSON file for each rule in the rules collection
    def generate(site)
      rules_collection = site.collections["rules"]
      rules_collection.docs.each do |page|
        rules_path = "#{site.dest}/rules/"
        ensure_directory(rules_path)

        file_name = "#{page.data['code']}.json"
        full_path = rules_path + file_name

        page_hash = Hash.new
        page_hash["code"] = page.data["code"]
        page_hash["message"] = page.data["message"]
        page_hash["links"] = page.data["links"]
        page_hash["content"] = page.content
        File.open(full_path, 'w') { |f| f.write(page_hash.to_json) }

        site.pages << Jekyll::JSONPost.new(site, site.dest, 'rules', file_name)
      end
    end

    def ensure_directory(path)
      FileUtils.mkdir_p(path)
    end
  end
end