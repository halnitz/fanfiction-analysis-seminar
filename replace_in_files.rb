def replace_in_files(dir, chars, subdirs=true)
    Dir[dir + '/*'].each do |file|
        if File.directory?(file)
            replace_in_files(file, chars, subdirs) if subdirs
        else
            replaced = File.read(file).delete(chars)
            File.write(file, replaced)
        end
    end
end

replace_in_files('tmp', "'")