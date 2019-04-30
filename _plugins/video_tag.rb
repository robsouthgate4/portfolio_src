module Jekyll
    class VideoTag < Liquid::Tag
  
      def initialize(tag_name, input, tokens)
        super
        @input = input
      end

      def lookup(context, name)
        lookup = context
        name.split(".").each { |value| lookup = lookup[value] }
        lookup
      end
  
      def render(context)

        input_split = split_params(@input)
        src = input_split[0].strip

        baseurl = "#{lookup(context, 'site.url')}"

        output = "<video controls autoplay>"
        output += "<source src='#{baseurl}/#{src}' type='video/mp4'>"
        output += "</video>"
      end

      def split_params(params)
        params.split("|")
      end

    end
  end
  
  Liquid::Template.register_tag('video_tag', Jekyll::VideoTag)